function display_grid_element(element_id, global_elements_id) {
        const display_element = document.getElementById(element_id);
        const hide_elements = document.getElementsByClassName(global_elements_id);

        for (var i = 0; i < hide_elements.length; i++) {
                hide_elements[i].style.display = 'none';
        }
        display_element.style.display = 'grid';
        console.log("Display: " + element_id)

}