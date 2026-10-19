import dearpygui.dearpygui as dpg

def setup(title, width, height):
    # Create screen
    dpg.create_context()
    dpg.create_viewport(title, width, height)

    # Initialize
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()

def close():
    # Clean up resources
    dpg.destroy_context()
