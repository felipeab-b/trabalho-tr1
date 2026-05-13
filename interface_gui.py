import gi
import matplotlib
matplotlib.use('GTK3Agg')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.figure import Figure
from simulador import simular

figura = Figure(figsize=(5, 2))
ax = figura.add_subplot(1, 1, 1)

def atualizar_tela(texto_recuperado, sinal):
    GLib.idle_add(label_resultado.set_text, f"Recebido: {texto_recuperado}")
    GLib.idle_add(plotar_sinal, sinal)

def plotar_sinal(sinal):
    ax.clear()
    ax.step(range(len(sinal)), sinal, where='post')
    ax.set_title("Sinal TX - NRZ Polar")
    ax.set_ylim(-1.5, 1.5)
    figura.canvas.draw()

def on_enviar(button):
    texto = entry.get_text()
    simular(texto, atualizar_tela)

window = Gtk.Window(title="SimulaRede")
window.set_default_size(600, 400)
window.connect("destroy", Gtk.main_quit)

box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
window.add(box)

entry = Gtk.Entry()
entry.set_placeholder_text("Digite o texto...")
box.pack_start(entry, False, False, 0)

button = Gtk.Button(label="Enviar")
button.connect("clicked", on_enviar)
box.pack_start(button, False, False, 0)

label_resultado = Gtk.Label(label="Aguardando...")
box.pack_start(label_resultado, False, False, 0)

canvas = FigureCanvas(figura)
box.pack_start(canvas, True, True, 0)

window.show_all()
Gtk.main()