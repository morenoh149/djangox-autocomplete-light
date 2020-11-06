/**
 * if a company does not exist in the database,
 * accept user input as a ticker request for backend to fetch from
 * data provider
 */

console.log('foo');
document.addEventListener('dal-init-function', function () {
    console.log('bar');
    yl.registerFunction('ticker_autocomplete_init', function ($, element) {
        var $element = $(element);
        // autocomplete function here
        console.log('I dont see this');
    });
  })