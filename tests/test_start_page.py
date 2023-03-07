import pytest
from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestStartPage:

    def test_add_item_to_cart(self, start_page):
        """
         -Description: Positive test to register new user
              - Pre-condition:
                 -Open start page
             - Steps:
                  Open product page
                  Add item to basket
                  Verify change button
                  Click on button "Details delivery"
                  CLick on button "Continue shopping"
                  Click on basket
                  Verify item into basket
        """
        start_page.add_item_to_cart()
