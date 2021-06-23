import os, shutil, logging, tempfile


def make_package(suffix=None):
    this_dir = os.path.dirname(os.path.abspath(__file__))
    dist_dir = os.path.join(this_dir, 'correosoficial')
    folder = dist_dir.split("\\")

    # Comprobamos si no existe el directorio a comprimir
    if not os.path.exists(dist_dir):
        print(f"No existe el directorio: {folder[-1]}")
    else:
        print(f"Se va a comprimir el directorio: {folder[-1]}")

    with tempfile.TemporaryDirectory() as tmpdir:
        shutil.copytree(
            os.path.join(this_dir, 'correosoficial'),
            os.path.join(tmpdir, 'correosoficial'),
            ignore = shutil.ignore_patterns('.git', 'phpdoc'))

        zip_name = 'correosoficial_1.0.0'
        if suffix:
            zip_name += '-' + suffix
        
        # Iniciamos logs
        logging.basicConfig(level = logging.DEBUG,
            format='%(asctime)s : %(levelname)s : %(message)s',
            filename = 'correosoficial.log',
            filemode = 'w',)
        logging.info("Inicio del proceso")

        # Empaquetamos
        shutil.make_archive(
            os.path.join('RELEASES_CorreosOficial', zip_name), 'zip', tmpdir, base_dir = "correosoficial", logger = logging)
        
        # Finalizamos logs
        logging.info("Fin del proceso")

# Llamamos a la función empaquetadora
make_package();
