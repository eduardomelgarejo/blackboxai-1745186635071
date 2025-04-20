from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ('paciente', 'Paciente'),
        ('profesional', 'Profesional'),
        ('ambos', 'Ambos'),
    ]
    nombre_completo = models.CharField(max_length=100, blank=True, null=True)
    correo = models.EmailField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    tipo_usuario = models.CharField(max_length=11, choices=TIPO_USUARIO_CHOICES)

class Profesional(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='profesional')
    especialidad = models.CharField(max_length=100)
    perfil = models.TextField(blank=True, null=True)

class FichaPaciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='ficha_paciente')
    rut = models.CharField(max_length=12, unique=True)
    antecedentes_medicos = models.TextField(blank=True, null=True)
    alergias = models.TextField(blank=True, null=True)
    medicamentos_actuales = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True)

class TurnoProfesional(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='turnos')
    fecha = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()

class SolicitudCambioTurno(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitudes_cambio_turno')
    motivo = models.TextField()
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)

class HistorialAtencion(models.Model):
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='historial_atenciones_paciente')
    profesional = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='historial_atenciones_profesional')
    fecha = models.DateField()
    motivo = models.TextField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()

class AlertaReserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='alertas_reserva')
    tipo_alerta = models.CharField(max_length=50)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

class Chat(models.Model):
    emisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='chats_enviados')
    receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='chats_recibidos')
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

class Box(models.Model):
    tipo_box = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    equipamiento = models.TextField()
    disponible = models.BooleanField(default=True)

class DisponibilidadBox(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name='disponibilidades')
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

class CentroAyuda(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='centro_ayuda')
    tipo_solicitud = models.CharField(max_length=50)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)

class Reserva(models.Model):
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reservas_paciente')
    profesional = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reservas_profesional')
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20)
