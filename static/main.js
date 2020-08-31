			$.fn.numpad.defaults.gridTpl = '<table style="transform: scale(2);" class="table modal-content"></table>';
			$.fn.numpad.defaults.backgroundTpl = '<div class="modal-backdrop in"></div>';
			$.fn.numpad.defaults.displayTpl = '<input type="text" class="form-control" />';
			$.fn.numpad.defaults.buttonNumberTpl =  '<button type="button" class="btn btn-default"></button>';
			$.fn.numpad.defaults.buttonFunctionTpl = '<button type="button" class="btn" style="width: 100%;"></button>';
			$.fn.numpad.defaults.onKeypadCreate = function(){$(this).find('.done').addClass('btn-primary');};

			// Instantiate NumPad once the page is ready to be shown
			$(document).ready(function(){
				$('#text-basic').numpad();
				$('#password').numpad({
					displayTpl: '<input class="form-control" type="password" />',
					hidePlusMinusButton: true,
					hideDecimalButton: true
				});
				$('#numpadButton-btn').numpad({
					target: $('#numpadButton')
				});
				$('#numpad4div').numpad();
				$('#numpad4column .qtyInput').numpad();

				$('#numpad4column tr').on('click', function(e){
					$(this).find('.qtyInput').numpad('open');
				});
			});