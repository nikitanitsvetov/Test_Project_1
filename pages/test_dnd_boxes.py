from dnd_boxes import DndBoxes
import pytest
import allure


@allure.feature('page elements')
def test_dnd_boxes_page_elements(browser):
    dnd_boxes = DndBoxes(browser)
    dnd_boxes.open()
    dnd_boxes.drag_element().is_displayed()
    dnd_boxes.drop_element().is_displayed()
    dnd_boxes.requirement().is_displayed()

@allure.feature('Drag and Drop functional')
def test_drag_and_drop_func(browser):
    dnd_boxes = DndBoxes(browser)
    dnd_boxes.open()
    dnd_boxes.drag_n_drop_func()
    dnd_boxes.success_message().is_displayed()

def requirement_messages():
    return[
        'There should be two squares on the page',
        'The bottom square must be draggable',
        'When dragging the bottom square to the top one, the text "Dropped!" should appear in the top square.',
        'The bottom square can only be dragged once'
    ]
@allure.feature('Requirements verification')
@pytest.mark.parametrize('requirement_messages', requirement_messages())
def test_requirement_messages_verify(browser, requirement_messages):
    dnd_boxes = DndBoxes(browser)
    dnd_boxes.open()
    dnd_boxes.requirement().click()
    dnd_boxes.requirements_text(requirement_messages).is_displayed()