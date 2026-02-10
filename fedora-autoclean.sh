#!/usr/bin/env bash
# Fedora Weekly Auto Clean Script
# Aman untuk SSD kecil & dev environment
# echo "user ALL=(ALL) NOPASSWD: /usr/sbin/dnf, /usr/sbin/journalctl, /usr/bin/journalctl, /usr/bin/du, /usr/sbin/du" | sudo tee /etc/sudoers.d/fedora-autoclean

set -e

echo "=== Fedora Auto Clean Started: $(date) ==="

# 1. Bersihkan DNF cache
echo "[*] Cleaning DNF cache..."
sudo dnf clean all -y

# 2. Hapus orphan packages
echo "[*] Removing orphan packages..."
sudo dnf autoremove -y

# 3. Batasi journal log (max 200MB)
echo "[*] Vacuuming journal logs..."
sudo journalctl --vacuum-size=200M

# 4. Flatpak unused runtime
if command -v flatpak &>/dev/null; then
    echo "[*] Removing unused Flatpak runtimes..."
    flatpak uninstall --unused -y || true
fi

# 5. User cache
echo "[*] Cleaning user cache (excluding mozilla)..."
find ~/.cache \
    -mindepth 1 \
    -maxdepth 1 \
    ! -name mozilla \
    -exec rm -rf {} + || true

# 6. Flatpak user cache
rm -rf ~/.var/app/*/cache/* 2>/dev/null || true

# 7. Go module cache (jika Go ada)
if command -v go &>/dev/null; then
    echo "[*] Cleaning Go module cache..."
    go clean -modcache || true
fi

# 8. npm cache (jika npm ada)
if command -v npm &>/dev/null; then
    echo "[*] Cleaning npm cache..."
    npm cache clean --force || true
fi

# 9. opencode snapshot (jika ada)
if [ -d "$HOME/.local/share/opencode/snapshot" ]; then
    echo "[*] Cleaning opencode snapshot..."
    rm -rf "$HOME/.local/share/opencode/snapshot"
fi

echo "[*] Cari folder terbesar di root..."
sudo du -xh / --max-depth=1 2>/dev/null | sort -h

echo "[*] Fokus ke /var..."
sudo du -xh /var --max-depth=1 | sort -h

echo "=== Fedora Auto Clean Finished: $(date) ==="
docker system df
echo "---List of all images stored on local system---"
docker image ls
echo "-----------------------------------------------"
df -h /
