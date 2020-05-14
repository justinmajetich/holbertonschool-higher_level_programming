window.onload = function () {
  const $myList = $('UL.my_list');

  // Add item
  $('DIV#add_item').click(() => {
    $myList.append('<li>Item</li>');
  });

  // Remove item
  $('DIV#remove_item').click(() => {
    const lastItem = $('UL.my_list LI').last();
    lastItem.remove();
  });

  // Clear list
  $('DIV#clear_list').click(() => {
    $myList.empty();
  });
};
