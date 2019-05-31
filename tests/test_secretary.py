__author__ = "María Andrea Vignau"
import sys
import os

sys.path.append(os.path.join(__file__, '../../src'))

from secretary import Renderer

from unittest import TestCase, mock

import models

templatepath = os.path.abspath(os.path.join(__file__, '../../templates'))


def search_on_templates(filename):
    path_real = os.path.join(templatepath, filename)
    path_test = os.path.join(__file__, "..", filename)

    if os.path.exists(path_test):
        return path_test
    elif os.path.exists(path_real):
        return path_real
    else:
        raise FileNotFoundError


class TestTemplates(TestCase):
    def test_default(self):
        engine = Renderer(media_path=templatepath)
        with open(search_on_templates('template.odt'), 'rb') as template:
            with open(search_on_templates('temp_output.odt'), 'wb') as output:
                output.write(engine.render(template, image='writer.png'))
        print("Template rendering finished! Check output.odt file.")

    def test_causa(self):
        s1 = models.sessions()
        causa = s1.query(models.TableCausa)[0]
        destinatario = causa.TableDestinatario
        print(destinatario)
        engine = Renderer(media_path=templatepath)
        with open(search_on_templates('mv-informepericial.odt'), 'rb') as template:
            with open('temp_informeelaborado.odt', 'wb') as output:
                output.write(engine.render(template, causa=causa))
        print("Template rendering finished! Check informeelaborado.odt file.")
