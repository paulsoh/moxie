(function(){
    $(document).ready(function(){

        $price_slider = $('#price-slider');
        $id_price = $('#id_price');
        $goal_slider = $('#goal-slider');
        $id_sales_goal = $('#id_sales_goal');
        $expected_sales = $('#expected-sales');

        $id_end_date = $('#id_end_date'); 

        
        // slider init
        $price_slider.slider();
        $goal_slider.slider();

        // date picker init
        var nowTemp = new Date();
        var now = new Date(nowTemp.getFullYear(), nowTemp.getMonth(), nowTemp.getDate(), 0, 0, 0, 0);
        var endDate = $id_end_date.datepicker({
            onRender: function(date) {
                return date.valueOf() < now.valueOf() ? 'disabled':'';
            }
        });
        
        $goal_slider.on('slide', function(position){
            $id_sales_goal.val(position.value);
        })
        $id_sales_goal.on('change', function(){
            $goal_slider.slider('setValue', $id_price.val());
        })
        $price_slider.on('slide', function(position){
            $id_price.val(position.value);
        })
        $id_price.on('change', function(){
            $price_slider.slider('setValue', $id_price.val());
        })

        $('#step-2').on('change slide', function(){
            $expected_sales.html("<h5> 예상 매출:"+$id_price.val()*$id_sales_goal.val()+"원</h5>");
        })

        // jquery file upload
        $("#id_thumbnail_image").fileinput({
            browseClass: "btn btn-primary btn-block",
            allowedFileExtensions: ["jpg", "gif", "png", "jpeg"],
            initialCaption: "JPG, JPEG, GIF, PNG 형식만 지원합니다",
            maxFileSize: 1024,
            showRemove: false,
            showUpload: false
        });

        $form_step_1 = $('#step-1');
        $form_step_2 = $('#step-2');
        $form_step_3 = $('#step-3');
        $step_1 = $('[data-step="1"]');
        $step_2 = $('[data-step="2"]');
        $step_3 = $('[data-step="3"]');
        $next_btn = $('#button-id-next'); 
        $prev_btn = $('#button-id-prev'); 
        $submit = $('#submit-id-submit');

        function atStepOne(){
            $step_1.removeClass('is-active is-complete');
            $step_2.removeClass('is-active is-complete');
            $step_3.removeClass('is-active is-complete');
            $step_1.addClass('is-active');
        }

        function atStepTwo(){
            $step_1.removeClass('is-active is-complete');
            $step_2.removeClass('is-active is-complete');
            $step_3.removeClass('is-active is-complete');
            $step_1.addClass('is-complete');
            $step_2.addClass('is-active');
        }

        function atStepThree(){
            $step_1.removeClass('is-active is-complete');
            $step_2.removeClass('is-active is-complete');
            $step_3.removeClass('is-active is-complete');
            $step_1.addClass('is-complete');
            $step_2.addClass('is-complete');
            $step_3.addClass('is-active');
        }

        // init 
        current_page = 1;
        $form_step_1.show();
        $form_step_2.hide();
        $form_step_3.hide();

        $prev_btn.hide();
        $next_btn.show();
        $submit.hide();

        atStepOne();

        $next_btn.on('click', function(){
            if(current_page===1){
                $form_step_1.hide();
                $form_step_2.show();
                $form_step_3.hide();

                $prev_btn.show();
                $next_btn.show();
                $submit.hide();

                atStepTwo();
            }else{
                $form_step_1.hide();
                $form_step_2.hide();
                $form_step_3.show();

                $prev_btn.show();
                $next_btn.hide();
                $submit.show();

                atStepThree();
            }
            current_page += 1;
        })
        $prev_btn.on('click', function(){
            if(current_page===2){
                $form_step_1.show();
                $form_step_2.hide();
                $form_step_3.hide();

                $prev_btn.hide();
                $next_btn.show();
                $submit.hide();

                atStepOne();
            }else{
                $form_step_1.hide();
                $form_step_2.show();
                $form_step_3.hide();

                $prev_btn.show();
                $next_btn.show();
                $submit.hide();

                atStepTwo();
            }
            current_page -= 1;
        })
    });
})();
