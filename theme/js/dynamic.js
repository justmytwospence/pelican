$(document).ready(function () {
    $('.Design').tooltip({
    	title: "The commonality between science and art is in trying to see profoundly - to develop strategies of seeing and showing. -Edward Tufte",
    	placement: "left",
    })
    $('.Misc').tooltip({
    	title: "Miscellania that doesn't fit anywhere else.",
    	placement: "left"
    })
    $('.Python').tooltip({
    	title: "Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.",
    	placement: "left"
    })

    $(function(){
        $('.navbar').data('size','big');
    });
    
    $(window).scroll(function(){
        var $nav = $('#header_nav');
        if ($('body').scrollTop() > 0) {
            if ($nav.data('size') == 'big') {
                $nav.data('size','small').stop().animate({
                    height:'40px'
                }, 600);
            }
        } else {
            if ($nav.data('size') == 'small') {
                $nav.data('size','big').stop().animate({
                    height:'100px'
                }, 600);
            }  
        }
    });

})