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
            $goal_slider.slider('setValue', $id_sales_goal.val());
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
    });
})();
