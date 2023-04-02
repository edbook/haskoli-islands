/*  Author: Abelardo Pardo (<abelardo.pardo@sydney.edu.au>) */
/* Version: 170726 */
/* Variable to allow for UID set by other means (additional code needed) */
var given_uid = '';
function dynsite_send_data(s, v, o) {
    var data = {}
    /* If loading locally, skip the logging */
    if (location.protocol == 'file:') {
	console.log('SEND:' + document.location.pathname + ',' +
                    DOCUMENTATION_OPTIONS.CONTEXT + ',' + v + ',' + JSON.stringify(o));
	return;
    }

    if (DOCUMENTATION_OPTIONS.DATA_CAPTURE_URL != '') {
        data[DOCUMENTATION_OPTIONS.DATA_CAPTURE_CONTEXT_NAME] = DOCUMENTATION_OPTIONS.CONTEXT;
        data[DOCUMENTATION_OPTIONS.DATA_CAPTURE_SUBJECT_NAME] = s;
        data[DOCUMENTATION_OPTIONS.DATA_CAPTURE_VERB_NAME] = v;
        data[DOCUMENTATION_OPTIONS.DATA_CAPTURE_OBJECT_NAME] = JSON.stringify(o);
        $.ajax({
	    'type': DOCUMENTATION_OPTIONS.DATA_CAPTURE_METHOD,
	    'url': DOCUMENTATION_OPTIONS.DATA_CAPTURE_URL,
	    'data': data
        });
    }
}
/*****  duration form submission **** */
$(document).ready(function() {
    function init() {
	/* This is button. Parent is the form element */
	var form_el = $(this).parent();
        var ok_icon = form_el.parent().children("img");

	$(this).click(function(e){
	    e.preventDefault();
	    data = {};
	    data['activity-id'] = form_el.find('input[name = "duration-id"]').val();
	    data['value'] = form_el.find('select[name = "duration-value"]').val();
	    dynsite_send_data(given_uid, "activity-duration", data);
	    form_el.hide()
	    ok_icon.show()
	    return false;  //stop the actual form post !important!
	});
    }
    $(".reauthoring_duration_submit").each(init)
});
/*****  Generic form submission **** */
$(document).ready(function() {
    function init() {
	/* This is button. Parent is the form element */
	var form_el = $(this).closest('form');
    var ok_icon = form_el.parent().children("img");
    var text_area = form_el.parent().find("textarea:first-of-type");
    var form_id = form_el.attr("id");

    if (form_id == null) {
        form_id = form_el.find("input[name='form_id']").attr("value");
    }
    if (form_id == null) {
        form_id = '';
    }
    if (text_area != null && DOCUMENTATION_OPTIONS.DATA_CAPTURE_URL != '') {
        data_request = {
            'type': 'GET',
            'url': DOCUMENTATION_OPTIONS.DATA_CAPTURE_URL + '/../get_attribute',
            'data': {'context': DOCUMENTATION_OPTIONS.CONTEXT,
                     'key': form_id + '_' + text_area.attr("name")
            }
        }

        $.ajax(data_request).done(function(data) {
            if (typeof data === 'string' && data != "") {
                text_area.text(data);
            }
        });
    }
	$(this).click(function(e){
	    e.preventDefault();
	    data = {};
	    /* This is the default event name */
	    event_name = "form-submit";
        /* Store some initial fields*/
        data['url'] = document.URL;
        data['form_id'] = form_id;
	    /* Loop over the input elements in the form */
	    form_el.find('*').filter(':input').each(function(){
            if (this.name == "") {
                return;
            }
            /* And this to catch the event name from within the form */
            if (this.name == "event-name") {
                event_name = this.value;
                return;
            }
            /* Accumulate the rest of input fields */
            if (((this.type != "radio") && (this.type != "checkbox")) || this.checked) {
                    /* data['id'] = this.name;
                data['answer'] = this.value; */
                data[this.name] = this.value;
            }
	    });
	    /* Send! */
	    dynsite_send_data(given_uid, event_name, data);
        /* If button has class reauthoring_reload, fire the reload */
        if ($(this).hasClass('reauthoring_reload')) {
            document.location.reload(true);
            return false;
        }
	    form_el.hide()
	    ok_icon.show()
	    return false;  //stop the actual form post !important!
	});
    }
    $(".reauthoring_submit").each(init)
});
/***** Expand collapse of sections *****/
$(document).ready(function (){
    function init(){
	// get header & section, and add static classes
	var header = $(this);
	var section = header.parent();
	header.addClass("html-toggle-button");

	// helper to test if url hash is within this section
	function contains_hash(){
	    var hash = document.location.hash;
	    return hash && (section[0].id == hash.substr(1) ||
			    section.find(hash.replace(/\./g,"\\.")).length>0);
	}

	// helper to control toggle state
	function set_state(expanded, track) {
	    if (expanded) {
		section.addClass("expanded").removeClass("collapsed");
		section.children().show();
		event_name = "expand";
	    } else {
		section.addClass("collapsed").removeClass("expanded");
		section.children().hide();
		/* for :ref: span tag */
		section.children("span:first-child:empty").show();
		header.show();
		event_name = "collapse";
	    }

	    if (track && DOCUMENTATION_OPTIONS.DATA_CAPTURE_URL) {
		data = {};
		data["page"] = document.URL.replace(/#.*$/, "");
		data["section"] = section.attr("id");
		data["operation"] = event_name;
		dynsite_send_data(given_uid, 'activity-collapse-expand', data);
	    }
	}

	// initialize state
	set_state(section.hasClass("expanded") || contains_hash(),
		  contains_hash());

	// bind toggle callback
	header.click(function (){
	    set_state(!section.hasClass("expanded"), true);
	    $(window).trigger('cloud-section-toggled', section[0]);
	});

	// open section if user jumps to it from w/in page
	$(window).bind("hashchange", function () {
            if(contains_hash()) set_state(true, true);
	});
    }

    // Apply to activity with section attribute
    $(".activity.section > h2, .activity.section > h3, .activity.section > h4, .activity.section > h5, .activity.section > h6").each(init);

    // Apply to chapter sections!
    $("div.chapter-with-expand > div.section > h1, div.chapter-with-expand > div.section > h2, div.chapter-with-expand > div.section > h3, div.chapter-with-expand > div.section > h4, div.chapter-with-expand > div.section > h5, div.chapter-with-expand > div.section > h6").each(init);
});
/***** Embedded MCQ *****/
function grade_mcq(div_el) {
    /* Get all the answer elements */
    answer_input = div_el.find("form > ol.eqt-answer-list > li input:checked");
    // If none is clicked, return -1
    if (answer_input.length == 0) {
	return -1;
    }
    // Return the answer
    if (answer_input[0].value == 'C') {
	return 1;
    }
    return 0;
}

function grade_mc(div_el) {
    /* Get all the answer elements */
    answers = div_el.find("form > ol.eqt-answer-list > li > input");
    /* Loop over input element of each answer */
    for (i = 0, max = answers.length; i < max; i++) {
	var answer = answers[i];
	/* Check if there has been a mistake */
	if ((answer.checked && answer.value == "I") ||
	    ((!answer.checked) && answer.value == "C")) {
	    // Mistake! Answer is incorrect
	    return 0;
	}
    }
    // No disagreement. Answer is correct
    return 1;
}

function grade_fib(div_el) {
    /* Find answer */
    var qval = div_el.find("form > div.reauthoring_embedded_quiz-fib-answer input[name = 'question']")[0].value;
    /* Empty answer prompts no action */
    if (qval == "") {
	return -1;
    }
    /* Find the given value */
    var aval = div_el.find("form > div.reauthoring_embedded_quiz-fib-answer input[name = 'solution']")[0].getAttribute("value");

    // If they agree, correct.
    if (qval == aval) {
	return 1;
    }

    // Incorrect
    return 0;
}

function grade() {
    /* Get the div element to process from above */
    var div_el = $(this).parent().parent();

    div_id = div_el[0].getAttribute('class');
    if (div_id.substring(div_id.length - 4, div_id.length) == "-fib") {
	answer = grade_fib(div_el);
    } else if (div_id.substring(div_id.length - 3, div_id.length) == "-mc") {
	answer = grade_mc(div_el);
    } else {
	answer = grade_mcq(div_el);
    }

    /* Grade button pushed with no answer given. Finish */
    if (answer == -1) {
	return;
    }

    buttons_el = div_el.find(".reauthoring_embedded_quiz_buttons");
    // If answer is correct, insert text in button and visualize icon
    if (answer == '1') {
	buttons_el.find(".correct_icon").css('opacity', '1');
	buttons_el.find(".reauthoring-embedded-answer").text(' Rétt!');
    } else {
	buttons_el.find(".incorrect_icon").css('opacity', '1');
	buttons_el.find(".reauthoring-embedded-answer").text(' Ekki rétt, reyndu aftur');
    }

    // Send the "embedded-question-grade" event
    data = {};
    data['question_id'] = div_el.attr('id');
    data['answer'] = answer;
    dynsite_send_data(given_uid, 'embedded-question', data);

    /* Change the visibility of the buttons */
    buttons_el.find(".reauthoring-grade").css('display', 'none');
    buttons_el.find(".reauthoring-again").css('display', 'inline');
    buttons_el.find(".reauthoring-solution").css('display', 'none');

    // Show all explanations if answer is correct.
    // Only show checked field explanations if answer is incorrect
    if (answer == '1') {
        div_el.find(".tip.expl").show();
    } else {
        div_el.find("form > ol.eqt-answer-list > li > input:checked").parent().find('.tip.expl').show();
    }
};

function again() {
    // Hide answer
    up_div = $(this).parent();
    up_div.find("img").css('opacity', '0');
    up_div.find(".reauthoring-embedded-answer").text('');
    // Change the buttons
    up_div.find(".reauthoring-grade").css('display', 'inline');
    up_div.find(".reauthoring-again").css('display', 'none');
    up_div.find(".reauthoring-solution").css('display', 'none');

    // Clean all the form fields
    up_up_div = $(this).parent().parent();
    up_up_div.find("form input").attr('checked', false);
    up_up_div.find("form input[type='text']").val('');

    // And the solutions
    up_up_div.find(".result_icon").css('display', 'none');
    up_up_div.find(".result_icon").css('display', 'none');
    up_up_div.find(".tip.expl").hide();
}

function solution_mcq(div_el) {
    /* Ordered list elements with the answer */
    div_el.find("form > ol.eqt-answer-list li").each(function() {
	$(this).find("img.result_icon").css('display', '');
    });
    div_el.find(".tip.expl").show();
    return;
}

function solution_fib(div_el) {
    /* Find answer value and set it to the value of the question field */
    var aval = div_el.find("form > div.reauthoring_embedded_quiz-fib-answer input[name = 'solution']")[0].getAttribute("value");
    div_el.find("form > div.reauthoring_embedded_quiz-fib-answer input[name = 'question']")[0].value = aval;
    div_el.find(".reauthoring_embedded_quiz_buttons img").css('opacity', '0');
    div_el.find(".reauthoring_embedded_quiz_buttons .reauthoring-embedded-answer").text('');
    div_el.find(".tip.expl").show();
}

function solution() {
    /* Get the div element to process from above */
    var div_el = $(this).parent().parent();

    div_id = div_el[0].getAttribute('class');
    if (div_id.substring(div_id.length - 4, div_id.length) == "-fib") {
	solution_fib(div_el);
    } else {
	solution_mcq(div_el);
    }

    // Send the "embedded-question-again" event
    data = {};
    data['question_id'] = div_el.attr('id');
    data['answer'] = "-1";
    dynsite_send_data(given_uid, 'embedded-question', data);
}

$(document).ready(function () {
    /* Get the buttons to execute the correct functions when clicked */
    var this_el = $('.reauthoring_embedded_quiz_buttons');
    this_el.find('.reauthoring-grade').click(grade);
    this_el.find('.reauthoring-grade').css('display', 'inline');
    this_el.find('.reauthoring-again').click(again);
    this_el.find('.reauthoring-solution').click(solution);
    this_el.find('.incorrect_icon').css('marginLeft','-23px');

    /* Background of the list and the correct/incorrect icons */
    this_el = $('.reauthoring_embedded_quiz_questions');
    this_el.find('li').css('background',
		      'none no-repeat 0 0').css('marginLeft', '2em');
    this_el.find('ol').css('listStyleType', 'upper-alpha');
    this_el.find('ul').css('listStyleType', 'upper-alpha');
});
/* XY Click widget */
$(document).ready(function() {
  $('div.xy_click img.xy_grid_img').each(function(e) {
    var offset = $(this).offset();
    var xoff = - $(this).width()/2;
    var yoff = $(this).height()/2;
    var ok_icon = $(this).parent().children('img.xy_ok_icon');
    var id_label = $(this).parent().parent().parent().parent().attr('id');
    data_request = {
            'type': 'GET',
            'url': DOCUMENTATION_OPTIONS.DATA_CAPTURE_URL + '/../get_attribute',
            'data': {'context': DOCUMENTATION_OPTIONS.CONTEXT,
                     'key': 'xy_click_' + id_label}
            };
    $.ajax(data_request).done(function(data) {
        if (data != "") {
            e_pageX = offset.left - xoff - ((data['x'] * xoff)/100);
            e_pageY = offset.top + yoff - ((data['y'] * yoff)/100);
            ok_icon.css('top', e_pageY - offset.top - 20);
            ok_icon.css('left', e_pageX - offset.left - 6);
            ok_icon.show();
        }
    });
  });
  $('div.xy_click img.xy_grid_img').click(function(e) {
    var offset = $(this).offset();
    var xoff = - $(this).width()/2;
    var yoff = $(this).height()/2;
    var ok_icon = $(this).parent().children('img.xy_ok_icon');
    data = {};
    data['id'] = $(this).parent().parent().parent().parent().attr('id');
    data['url'] = document.URL;
    data['title'] = $(document).find('title').text()
    data['x'] = Math.round(100 * (e.pageX - offset.left + xoff)/-xoff);
    data['y'] = Math.round(100 * (yoff - (e.pageY - offset.top))/yoff);
    dynsite_send_data(given_uid, "xy-click", data);
    ok_icon.css('top', e.pageY - offset.top - 20);
    ok_icon.css('left', e.pageX - offset.left - 6);
    ok_icon.show();
  });
});
/* Page now records an event upon loading */
$(document).ready(function() {
    data = {};
    data['url'] = document.URL;
    dynsite_send_data(given_uid, "resource-view", data);
});
