# https://docs.python.org/3/library/shutil.html
# https://www.programcreek.com/python/example/7403/shutil.ignore_patterns
import os, shutil, logging
import tempfile

def make_package(suffix=None):
    this_dir = os.path.dirname(os.path.abspath(__file__))
    dist_dir = os.path.join(this_dir, 'correosoficial')

    # Comprobamos si no existe el directorio releases y lo creamos
    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)

    with tempfile.TemporaryDirectory() as tmpdir:
        shutil.copytree(
            os.path.join(this_dir, 'correosoficial'),
            os.path.join(tmpdir, 'correosoficial'),
            ignore=shutil.ignore_patterns('.git', 'phpdoc'))

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

make_package();

