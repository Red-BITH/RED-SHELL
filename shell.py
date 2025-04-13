#!/bin/bash

echo "[+] Openbox ve gerekli paketler kaldırılıyor..."
# LXQt ve Openbox'ın tüm paketlerini temizliyoruz
sudo xbps-remove -R openbox openbox-session openbox-themes tint2 picom feh conky

echo "[+] Gereksiz bağımlılıklar temizleniyor..."
sudo xbps-remove -o

echo "[+] Xorg ve Openbox yeniden kuruluyor..."
# Xorg ve Openbox'ı yeniden kuruyoruz
sudo xbps-install -y xorg openbox obconf tint2 rofi picom feh conky lightdm

echo "[+] Openbox için gerekli yapılandırma dosyaları oluşturuluyor..."

# .xinitrc dosyasını oluşturuyoruz
echo "exec openbox-session" > ~/.xinitrc

# LightDM konfigürasyonu için gerekli dosyayı ayarlıyoruz
echo "[+] LightDM'yi yapılandırıyoruz..."
sudo systemctl enable lightdm

# Openbox için autostart dosyasını oluşturuyoruz
mkdir -p ~/.config/openbox
cat > ~/.config/openbox/autostart <<EOF
# Openbox autostart
tint2 &
picom --config ~/.config/picom/picom.conf &
feh --bg-scale ~/Pictures/wallpapers/wall.jpg &
conky &
EOF

# Picom için basit bir konfigürasyon dosyası oluşturuyoruz
mkdir -p ~/.config/picom
cat > ~/.config/picom/picom.conf <<EOF
backend = "xrender";
vsync = true;
shadow = true;
fading = true;
fade-delta = 4;
EOF

# Tint2 için temel ayar dosyasını oluşturuyoruz
mkdir -p ~/.config/tint2
cat > ~/.config/tint2/tint2rc <<EOF
# Basit tint2 panel config (tema sonrası özelleştirilebilir)
panel_items = TSC
panel_size = 100% 30
panel_margin = 0 0
panel_padding = 6 6 6
EOF

# Wallpaper için varsayılan bir görsel indiriyoruz
mkdir -p ~/Pictures/wallpapers
curl -s https://picsum.photos/1920/1080 -o ~/Pictures/wallpapers/wall.jpg

echo "[✓] Kurulum tamamlandı! Openbox, LightDM, Tint2, Picom ve Conky kuruldu."
echo "➡️ LightDM üzerinden oturum açarak Openbox'ı seçebilirsin."
