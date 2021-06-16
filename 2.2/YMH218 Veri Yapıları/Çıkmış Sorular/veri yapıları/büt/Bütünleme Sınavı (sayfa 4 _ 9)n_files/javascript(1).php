M.core_scroll_manager=M.core_scroll_manager||{};M.core_scroll_manager.save_scroll_pos=function(Y,element){if(typeof(element)=='string'){element=Y.one(document.getElementById(element))}
var form=element.ancestor('form');if(!form){return}
var scrollpos=form.one('input[name=scrollpos]');if(!scrollpos){scrollpos=form.appendChild(form.create('<input type="hidden" name="scrollpos" />'))}
scrollpos.set('value',form.get('docScrollY'))}
M.core_scroll_manager.save_scroll_action=function(e){var link=e.target.ancestor('a[href]');if(!link){M.core_scroll_manager.save_scroll_pos({},e.target);return}
link.set('href',link.get('href')+'&scrollpos='+link.get('docScrollY'))}
M.core_scroll_manager.scroll_to_saved_pos=function(Y){var matches=window.location.href.match(/^.*[?&]scrollpos=(\d*)(?:&|$|#).*$/,'$1');if(matches){window.scrollTo(0,matches[1]);Y.on('domready',function(){window.scrollTo(0,matches[1])});if(Y.one('body').hasClass('ie')){M.core_scroll_manager.force_ie_to_scroll(Y,matches[1])}}}
M.core_scroll_manager.force_ie_to_scroll=function(Y,targetpos){var hackcount=25;function do_scroll(){window.scrollTo(0,targetpos);hackcount-=1;if(hackcount>0){setTimeout(do_scroll,10)}}
Y.on('load',do_scroll,window)}
M.core_question_engine=M.core_question_engine||{};M.core_question_engine.questionformalreadysubmitted=!1;M.core_question_engine.init_submit_button=function(Y,button,slot){var buttonel=document.getElementById(button);Y.on('click',function(e){M.core_scroll_manager.save_scroll_pos(Y,button);buttonel.form.action=buttonel.form.action+'#q'+slot},buttonel)}
M.core_question_engine.init_form=function(Y,form){Y.one(form).setAttribute('autocomplete','off');Y.on('submit',M.core_question_engine.prevent_repeat_submission,form,form,Y);Y.on('key',function(e){if(!e.target.test('a')&&!e.target.test('input[type=submit]')&&!e.target.test('input[type=img]')&&!e.target.test('textarea')&&!e.target.test('[contenteditable=true]')){e.preventDefault()}},form,'press:13');Y.one(form).all('.questionflagsavebutton').remove();M.core_scroll_manager.scroll_to_saved_pos(Y)}
M.core_question_engine.prevent_repeat_submission=function(e,Y){if(M.core_question_engine.questionformalreadysubmitted){e.halt();return}
setTimeout(function(){Y.all('input[type=submit]').set('disabled',!0)},0);M.core_question_engine.questionformalreadysubmitted=!0}