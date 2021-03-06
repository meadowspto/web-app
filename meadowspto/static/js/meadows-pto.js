var MeadowsPTA = {};

$(function() {
  MeadowsPTA.eventAdminForm();
  MeadowsPTA.googleAnalytics();
  MeadowsPTA.crabfeed();
  MeadowsPTA.tinymce();
});

MeadowsPTA.tinymce = function() {
  tinymce.init({
      selector: 'textarea',
      toolbar: 'bold italic underline strikethrough link unlink image bullist numlist outdent indent blockquote subscript superscript | alignleft aligncenter alignright alignjustify styleselect formatselect fontselect fontsizeselect',
      width: 900,
      height: 400,
      plugins: 'link image',
  });
};

/*
Meadows.statusMessageManager = function() {
    if (_displayStatusMessage) {
        $('#status-message').slideDown(750);

        setTimeout(function() {
            $('#status-message').slideUp(1500);
        }, 5000);
    }
};
*/

MeadowsPTA.eventAdminForm = function() {
  $('#id_is_all_day').change(function() {
    if ($(this).prop('checked')) {
      $('#id_start_date_1').val('00:00:00');
      $('#id_end_date_1').val('00:00:00');
    } else {
      $('#id_start_date_1').val('');
      $('#id_end_date_1').val('');
    }
  });
}

MeadowsPTA.googleAnalytics = function() {
  $('.membership-form-download-button').click(function() {
    _gaq.push(['_trackEvent', 'Links', 'Click', 'Membership Form Download Button']);
  });
}

MeadowsPTA.crabfeed = function() {
  $('#crabfeed-tickets .event-ticket-quantity').change(function() {
    var quantity = $(this).val();
    $('.pp-event-ticket-quantity').val(quantity);
  });

  $('#crabfeed-tickets .raffle-ticket-quantity').change(function() {
    var quantity = $(this).val();
    $('.pp-raffle-ticket-quantity').val(quantity);
  });

  $('#crabfeed-tickets .raffle-pack-quantity').change(function() {
    var quantity = $(this).val();
    $('.pp-raffle-pack-quantity').val(quantity);
  });
}

function Utils() {
  var that = {};

  that.dateFormat = function(date) {
    var dateObj = new Date(date);
    return dateObj.toLocaleDateString();
  }

  return that;
}