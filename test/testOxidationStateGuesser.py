import unittest
import numpy.testing as np
from CompositionEntry import CompositionEntry
from utils.LookUpData import LookUpData
from utils.OxidationStateGuesser import OxidationStateGuesser

class testOxidationStateGuesser(unittest.TestCase):
    def test_guesser(self):
        ox = OxidationStateGuesser()
        ox.set_oxidationstates(LookUpData.load_special_property(
            "OxidationStates", lookup_dir="../lookup-data/"))
        ox.set_electronegativity(LookUpData.load_property(
            "Electronegativity", lookup_dir="../lookup-data/"))

        res = ox.get_possible_states(CompositionEntry(composition="NaCl"))
        self.assertEquals(1, len(res))
        np.assert_array_equal([1, -1], res[0])

        res = ox.get_possible_states(CompositionEntry(composition="Fe2O3"))
        self.assertEquals(1, len(res))
        np.assert_array_equal([3, -2], res[0])

        res = ox.get_possible_states(CompositionEntry(composition="NaHCO3"))
        self.assertEquals(1, len(res))
        np.assert_array_equal([10, 0, 5, 7], CompositionEntry(
            composition="NaHCO3").get_element_ids())
        np.assert_array_equal([1, 1, 4, -2], res[0])

        res = ox.get_possible_states(CompositionEntry(composition="NH3"))
        self.assertEquals(2, len(res))
        np.assert_array_equal([0, 6], CompositionEntry(
            composition="NH3").get_element_ids())
        np.assert_array_equal([1, -3], res[0])

        res = ox.get_possible_states(CompositionEntry(composition="NaAl"))
        self.assertEquals(0, len(res))

        res = ox.get_possible_states(CompositionEntry(composition="PbTiO3"))
        self.assertEquals(2, len(res))
        np.assert_array_equal([21, 81, 7], CompositionEntry(
            composition="PbTiO3").get_element_ids())
        np.assert_array_equal([4, 2, -2], res[0])