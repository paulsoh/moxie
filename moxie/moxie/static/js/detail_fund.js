(function(){
    $(document).ready(function(){
        // settings for toggle field
        $toggle_field = $('#toggle-field');
        $toggle_btn = $('#toggle-btn');
        $toggle_btn_fund = $('#toggle-btn-fund');
        idea_id = $toggle_btn_fund.data('idea-id');

        // input fields 
        $funder_name = $('#funder_name');
        $funder_address = $('#funder_address');
        $funder_cellphone = $('#funder_cellphone');
        $funder_quantity = $('#funder_quantity');

        // update fields when funding happens
        $current_funders = $('#current_funders');
        $current_quantity = $('#current_quantity');
        $current_progress = $('#current_progress');

        // settings for ajax - getting cookie
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        } 

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        
        function updateIdeaData(data){
            $current_funders.html(data.get_current_funders)
            $current_quantity.html(data.get_current_quantity)
            $current_progress.attr('style', 'width:'+data.get_current_progress+"%")
        }

        var csrftoken = getCookie('csrftoken');

        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        $toggle_btn_fund.click(function(){
            data={
                "funder_name": $funder_name.val(),
                "funder_address": $funder_address.val(),
                "funder_cellphone": $funder_cellphone.val(),
                "quantity": $funder_quantity.val(),
            }
            $.ajax({
                url: "/ideas/explore/" + idea_id + "/fund/",
                type: "POST",
                data: data,             
            })
            .done(function(data, textStatus, jqXHR){
                // to get idea data
                $funder_name.val('');
                $funder_address.val('');
                $funder_cellphone.val('');
                $funder_quantity.val('');
                $.ajax({
                    url: "/ideas/explore/" + idea_id + "/fund/",
                    type: "GET",
                })
                .done(function(data, textStatus, jqXHR){
                    console.log("Http request suceeded: "+jqXHR.status, data);
                    updateIdeaData(data)
                })

            })
            .fail(function(jqXHR, textStatus, errorThrown){
                console.log("Http request suceeded: "+jqXHR.status);
                console.log(textStatus);
                console.log(errorThrown);
            })
        });

        // ADDING EVENTS
        // toggle field and button event
        $toggle_btn.on('click', function(){
            console.log('BTN CLICKED');
            $toggle_field.toggleClass('fund-info-input'); 
            $toggle_btn_fund.toggle(); 
            if($toggle_field.hasClass('fund-info-input')){
                $toggle_btn.html('구매 정보 닫기');
            } else {
                $toggle_btn.html('구매 정보 보기');
            }
        });
    });
})();
