# Copyright 2018 María Andrea Vignau
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# For further info,

import os
from unittest import TestCase, mock
import models

class TestModels(TestCase):
    """Tests for models module.

    I mock filepath of database, creating a fake db to make tests."""

    TEMP_FILENAME = ":memory:"

    @classmethod
    def setUpClass(cls):
        """Set up. Patch FILEPATH. Creates a fake config."""
        cls.config_patch = mock.patch("models.FILEPATH")
        cls.config_patch = mock.patch("models.SQLALCHEMY_ECHO")
        models.FILEPATH = cls.config_patch.start()
        models.FILEPATH = cls.TEMP_FILENAME
        models.SQLALCHEMY_ECHO = cls.config_patch.start()
        models.SQLALCHEMY_ECHO = True

        # after changing filepath, reconnect to database
        models.init_engine()

    @classmethod
    def tearDownClass(cls):
        """Remove temporary config file."""
        if os.path.exists(cls.TEMP_FILENAME):
            print("Remove {}".format(cls.TEMP_FILENAME))
            os.remove(cls.TEMP_FILENAME)
        cls.config_patch.stop()

    def test_a_estadocausa(self):
        tipos = ["Ingresado", "Asignado", "En confección", "Terminado"]
        s1 = models.sessions()
        s1.add_all([models.TableEstadoCausa(descripcion=x) for x in tipos])
        s1.commit()
        nro = s1.query(models.TableEstadoCausa).count()
        self.assertEqual(nro, len(tipos), "No agrego todos los estados")

    def test_b_causa(self):
        """Crear una causa."""
        s1 = models.sessions()
        rows = [models.TableCausa(idCausa=1,
                                  expteJud="123-15",
                                  exptePol="1234",
                                  expteOtro="zzz",
                                  idEstado=s1.query(models.TableEstadoCausa)[0].id,
                                  caratula="Perez Jose s/pavada"
                                  ),]
        s1.add_all(rows)
        s1.commit()
        nro = s1.query(models.TableCausa).count()
        self.assertEqual(nro, len(rows), "No agrego todas las causas")


    def test_c_escritos(self):
        """Agregarle escritos"""
        s1 = models.sessions()
        rows = [models.TableEscrito(
            idCausa=s1.query(models.TableCausa)[0].idCausa,
            idEscrito=1,
            descripcion="oficio NN",
            ubicacionFisica="kkk"
        ),models.TableEscrito(
            idCausa=s1.query(models.TableCausa)[0].idCausa,
            idEscrito=2,
            descripcion="oficio NN+1",
            ubicacionFisica="lll"
        )]
        s1.add_all(rows)
        s1.commit()
        nro = s1.query(models.TableEscrito).count()
        self.assertEqual(nro, len(rows), "No agrego todos los escritos")

    def test_d_objeto(self):
        """Creo objetos"""
        s1 = models.sessions()
        rows = [models.TableObjeto(
            objetoRelacionado=None,
            descripcion="computadora negra",
            ubicacionFisica="kkk"
        ),models.TableObjeto(
            objetoRelacionado=None,
            descripcion="celular samsung",
            ubicacionFisica="ppp"
        ),models.TableObjeto(
            objetoRelacionado=None,
            descripcion="computadora blanca",
            ubicacionFisica="ppp"
        ),models.TableObjeto(
            objetoRelacionado=None,
            descripcion="celular nokia",
            ubicacionFisica="ppp"
        )]
        s1.add_all(rows)
        s1.commit()
        nro = s1.query(models.TableObjeto).count()
        self.assertEqual(nro, len(rows), "No agrego todos los objetos")

    def test_e_objetorelacionado(self):
        """Agrego objetos relacionados a otros objetos"""
        s1 = models.sessions()
        nro_anterior = s1.query(models.TableObjeto).count()
        rows = [models.TableObjeto(
            objetoRelacionado=s1.query(models.TableObjeto)[0].idObjeto,
            descripcion="disco rígido compu negra",
            ubicacionFisica="kkk"
        ),models.TableObjeto(
            objetoRelacionado=s1.query(models.TableObjeto)[1].idObjeto,
            descripcion="disco rígido compu blanca",
            ubicacionFisica="kkk"
        )]
        s1.add_all(rows)
        s1.commit()
        nro = s1.query(models.TableObjeto).count()
        self.assertEqual(nro, nro_anterior+len(rows), "No agrego todos los objetos")

    def test_f_relobjetoescrito(self):
        """Agrego objetos relacionados a escritos"""
        s1 = models.sessions()
        escritos = s1.query(models.TableEscrito)
        objetos = s1.query(models.TableObjeto)
        rows = [models.TableRelEscObj(
                idCausa=escritos[0].idCausa,
                idEscrito=escritos[0].idEscrito,
                idObjeto=objetos[0].idObjeto
        ), models.TableRelEscObj(
                idCausa=escritos[0].idCausa,
                idEscrito=escritos[0].idEscrito,
                idObjeto=objetos[1].idObjeto
        ), models.TableRelEscObj(
                idCausa=escritos[1].idCausa,
                idEscrito=escritos[1].idEscrito,
                idObjeto=objetos[2].idObjeto
        ), models.TableRelEscObj(
                idCausa=escritos[1].idCausa,
                idEscrito=escritos[1].idEscrito,
                idObjeto=objetos[3].idObjeto
        )]
        s1.add_all(rows)
        s1.commit()
        nro = s1.query(models.TableRelEscObj).count()
        self.assertEqual(nro, len(rows), "No agrego todas las relaciones escrito objeto")

    def test_g_relobjetoescrito(self):
        s1 = models.sessions()
        idCausa = s1.query(models.TableCausa)[0].idCausa
        objetos = models.objects_rel_causa(idCausa)

        relaciones = s1.query(models.TableRelEscObj).\
            filter(models.TableRelEscObj.idCausa == idCausa).all()
        self.assertEqual(len(relaciones), len(objetos.all()))
