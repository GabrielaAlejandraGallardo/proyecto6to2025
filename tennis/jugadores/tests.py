from django.test import TestCase, Client
from django.urls import reverse
from datetime import date
from .models import Jugador
from tennis.cuota.models import Cuota

class JugadoresViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Crear jugador sin cuota
        self.jugador1 = Jugador.objects.create(
            DNI='12345678A',
            nom='Jugador Uno',
            fechan=date(2000, 1, 1),
            altura=180,
            peso=75,
            dire='Calle Falsa 123',
            cd='28001',
            talla='M',
            descripcion='Tenis'
        )
        # Crear jugador con cuota al día
        self.jugador2 = Jugador.objects.create(
            DNI='87654321B',
            nom='Jugador Dos',
            fechan=date(1995, 5, 5),
            altura=175,
            peso=70,
            dire='Avenida Siempre Viva 742',
            cd='28002',
            talla='L',
            descripcion='Tenis'
        )
        self.cuota_al_dia = Cuota.objects.create(
            jugador=self.jugador2,
            cuotaMes=date.today()
        )

        # Crear jugador con cuota pendiente (mes anterior)
        self.jugador3 = Jugador.objects.create(
            DNI='11223344C',
            nom='Jugador Tres',
            fechan=date(1990, 3, 3),
            altura=170,
            peso=68,
            dire='Calle Luna 456',
            cd='28003',
            talla='S',
            descripcion='Tenis'
        )
        mes_anterior = date.today().replace(day=1)
        if mes_anterior.month == 1:
            mes_anterior = mes_anterior.replace(year=mes_anterior.year-1, month=12)
        else:
            mes_anterior = mes_anterior.replace(month=mes_anterior.month-1)
        self.cuota_pendiente = Cuota.objects.create(
            jugador=self.jugador3,
            cuotaMes=mes_anterior
        )

    def test_lista_view_status_code(self):
        response = self.client.get(reverse('lista'))
        self.assertEqual(response.status_code, 200)

    def test_lista_view_context(self):
        response = self.client.get(reverse('lista'))
        jugadores = response.context['jugadores']
        self.assertEqual(len(jugadores), 3)

        for jugador in jugadores:
            if jugador.id == self.jugador1.id:
                self.assertFalse(jugador.esta_al_dia)
            elif jugador.id == self.jugador2.id:
                self.assertTrue(jugador.esta_al_dia)
            elif jugador.id == self.jugador3.id:
                self.assertFalse(jugador.esta_al_dia)

    def test_lista_template_content(self):
        response = self.client.get(reverse('lista'))
        content = response.content.decode('utf-8')
        self.assertIn('Al día con las cuotas', content)
        self.assertIn('Debe cuotas', content)
