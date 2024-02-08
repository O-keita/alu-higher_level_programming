#!/usr/bin/node

$(document).ready(function () {
  $('div#add_item').click(() => {
    newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
  });

  $('div#remove_item').on('click', () => {
    $('ul.my_list li:last-child').remove();
  });

  $('div#clear_list').on('click', () => {
    $('ul.my_list').empty();
  });
});
