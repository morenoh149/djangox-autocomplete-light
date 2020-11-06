console.log('foo');
document.addEventListener('dal-init-function', function () {
    console.log('bar');
    yl.registerFunction('ticker_autocomplete_init', function ($, element) {
        var $element = $(element);
        // autocomplete function here
        console.log('I dont see this');
    });
  })