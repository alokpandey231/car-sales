function searchOpen() {
  console.log("hi")
    var search = $('#search').val()
    var data = {
        search: search
    };
    $.ajax({
        url: 'ajax_search/',
        data: data,
        success: function (data) {
        fakedata = ['test1','test2','test3','test4','ietsanders'];
        console.log(data);
        $("#search").autocomplete({
        source: data,
        minLength: 0
        });
      }
    });
}
$( document ).ready(function() {
  var search = $('#search').val()
  var data = {
      search: search
  };
  $.ajax({
      url: 'ajax_search/',
      data: data,
      success: function (data) {
      fakedata = ['test1','test2','test3','test4','ietsanders'];
      console.log(data);
      $("#search").autocomplete({
      source: data,
      minLength: 0
      });
    }
  });
    console.log( "ready!" );
});
