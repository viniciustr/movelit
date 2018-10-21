$(document).ready(function() {
    var rw = document.getElementById('rootwizard');
    if (rw) {
        $(rw).bootstrapWizard({onTabShow: function(tab, navigation, index) {
            var $total = navigation.find('li').length;
            var $current = index+1;
            var $percent = ($current/$total) * 100;
            $('#rootwizard .progress-bar').css({width:$percent+'%'});
        }});
    }
});
