DISTRO=""

if [ -f "/etc/os-release" ]; then
    DISTRO=$(grep -oP '(?<=^ID=).+' /etc/os-release | tr -d '"')
fi

case "$DISTRO" in

    arch|manjaro|debian|ubuntu)
        echo "Arch Linux | vcpkg"
        INCLUDE_DIR="include"
        VCPKG_DIR="$INCLUDE_DIR/vcpkg"
        TA_LIB_DIR="$INCLUDE_DIR/ta-lib"

        mkdir -p "$INCLUDE_DIR"

        if [ ! -d "$VCPKG_DIR" ]; then
            echo "Клонируем vcpkg..."
            git clone https://github.com/microsoft/vcpkg.git "$VCPKG_DIR"
            cd "$VCPKG_DIR" || exit 1
            ./bootstrap-vcpkg.sh
            ./vcpkg integrate install
        else
            echo "vcpkg уже скачан"
            cd "$VCPKG_DIR" || exit 1
        fi

        ./vcpkg install cpprestsdk
        ./vcpkg install nlohmann-json

        if [ ! -d "$TA_LIB_DIR" ]; then
            echo "Клонируем ta-lib..."
            git clone https://aur.archlinux.org/ta-lib.git "$TA_LIB_DIR"
            cd "$TA_LIB_DIR" || exit 1
            makepkg -si
        else
            echo "ta-lib уже скачан"
            cd "$TA_LIB_DIR" || exit 1
        fi
        ;;

    *)
        echo "Дистрибутив не поддерживается данным install.sh. Доступные дистрибутивы: Arch | Manjaro | Debian | Ubuntu "
        exit 1
        ;;
esac

