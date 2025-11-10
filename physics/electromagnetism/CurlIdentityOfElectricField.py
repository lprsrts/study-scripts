# 2B kesitte (z=0) E, curl E ve curl curl E alanlarını üretip çizeceğim.
# E: karışık (hem düzlem içi hem de düzlem dışı) bileşenler içerir ki curl E'nin düzlem içi bileşenleri görülsün.
# Formül seçimi (k=1):
#   ψ(x,y) = sin(x) sin(y)
#   E = (-∂ψ/∂y, ∂ψ/∂x, α ψ) = (-cos(y) sin(x), cos(x) sin(y), α sin(x) sin(y))
#   curl E = ( ∂Ez/∂y, -∂Ez/∂x, ∂Ey/∂x - ∂Ex/∂y )
#           = ( α cos(y) sin(x), -α cos(x) sin(y), -2 sin(x) sin(y) )
#   curl curl E (analitik türev):
#           = ( -2 sin(x) cos(y),  2 cos(x) sin(y),  2 α sin(x) sin(y) )
#
# Her alan için:
#   - Düzlem içi (x,y) bileşenleri ok (quiver) ile
#   - Düzlem dışı bileşen (z) arkaplanda imshow ile
#   - Ayrı ayrı üç figür (kurala uygun: her grafik kendi başına)
#   - Dosyaya da kaydediyorum.

import numpy as np
import matplotlib.pyplot as plt
import os

# Parametreler
alpha = 0.7
n = 25
x = np.linspace(-2*np.pi, 2*np.pi, n)
y = np.linspace(-2*np.pi, 2*np.pi, n)
X, Y = np.meshgrid(x, y, indexing="xy")

# Yardımcı trig kısayollar
sinx = np.sin(X)
siny = np.sin(Y)
cosx = np.cos(X)
cosy = np.cos(Y)

# 1) E alanı
Ex = -cosy * sinx
Ey =  cosx * siny
Ez =  alpha * sinx * siny

# 2) curl E
Cx =  alpha * cosy * sinx
Cy = -alpha * cosx * siny
Cz = -2.0 * sinx * siny

# 3) curl curl E
Dx = -2.0 * sinx * cosy
Dy =  2.0 * cosx * siny
Dz =  2.0 * alpha * sinx * siny

# Ortak çizim yordamı
import os

def draw_field(U, V, W, title, fname):
    # Klasör yoksa oluştur
    output_dir = os.path.dirname(fname)
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    plt.figure(figsize=(7, 6))
    # Arkaplan: W (düzlem dışı bileşen)
    plt.imshow(W, extent=[x.min(), x.max(), y.min(), y.max()], origin="lower", aspect="equal")
    # Oklar: (U,V) düzlem içi
    step = 1  # tüm noktaları çiziyoruz; istenirse 2 yapılarak seyreltilebilir
    plt.quiver(X[::step, ::step], Y[::step, ::step], U[::step, ::step], V[::step, ::step])
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.savefig(fname, dpi=160)
    plt.show()

draw_field(Ex, Ey, Ez, "E alanı (oklar: Ex,Ey; arkaplan: Ez)", "output_images/E_field.png")
draw_field(Cx, Cy, Cz, "curl E (oklar: Cx,Cy; arkaplan: Cz)", "output_images/curlE_field.png")
draw_field(Dx, Dy, Dz, "curl curl E (oklar: Dx,Dy; arkaplan: Dz)", "output_images/curlcurlE_field.png")

print("Dosyalar kaydedildi: output_images/E_field.png, output_images/curlE_field.png, output_images/curlcurlE_field.png")
