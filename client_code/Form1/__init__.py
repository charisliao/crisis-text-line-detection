from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_area_1.text: 
      message = self.text_area_1.text 
      result = anvil.server.call("sentiment", message)
      self.label_4.text = result 
    else: 
      anvil.Notification("Please enter or paste some text", timeout=2).show()
    
    

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    message = self.text_area_1.text
    predicted_suicide_prob = anvil.server.call("sentiment", message)
    normal = self.radio_button_1.selected
    urgent = self.radio_button_2.selected
    app_tables.feedback.add_row(
    message=message, 
    predicted_suicide_prob=predicted_suicide_prob, 
    normal=normal,
    urgent=urgent,
    )
    self.clear_inputs()

    
  def clear_inputs(self):
    self.text_area_1.text = ""
    self.label_4.text = ""
    self.radio_button_1.selected = False
    self.radio_button_2.selected = False
    pass

    




