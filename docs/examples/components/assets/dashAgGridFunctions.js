var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.DatePicker = class {

    // gets called once before the renderer is used
  init(params) {
    // create the cell
    this.eInput = document.createElement('input');
    this.eInput.value = params.value;
    this.eInput.classList.add('ag-input');
    this.eInput.style.height = 'var(--ag-row-height)';
    this.eInput.style.fontSize = 'calc(var(--ag-font-size) + 1px)';

    // https://jqueryui.com/datepicker/
    $(this.eInput).datepicker({
      dateFormat: 'dd/mm/yy',
      onSelect: () => {
        this.eInput.focus();
      },
    });
  }

  // gets called once when grid ready to insert the element
  getGui() {
    return this.eInput;
  }

  // focus and select can be done after the gui is attached
  afterGuiAttached() {
    this.eInput.focus();
    this.eInput.select();
  }

  // returns the new value after editing
  getValue() {
    return this.eInput.value;
  }

  // any cleanup we need to be done here
  destroy() {
    // but this example is simple, no cleanup, we could
    // even leave this method out as it's optional
  }

  // if true, then this editor will appear in a popup
  isPopup() {
    // and we could leave this method out also, false is the default
    return false;
  }
}



// Used in the conditional rendering example
dagfuncs.moodOrGender = function (params) {
  var dagcomponentfuncs = window.dashAgGridComponentFunctions
           const moodDetails = {
              component: dagcomponentfuncs.MoodRenderer,
            };
            const genderDetails = {
              component: dagcomponentfuncs.GenderRenderer,
            };
            if (params.data) {
              if (params.data.type === 'gender') return genderDetails;
              else if (params.data.type === 'mood') return moodDetails;
            }
            return undefined;
}




dagfuncs.NumberInput = class {
    // gets called once before the renderer is used
  init(params) {
    // create the cell
    this.eInput = document.createElement('input');
    this.eInput.value = params.value;
    this.eInput.style.height = 'var(--ag-row-height)';
    this.eInput.style.fontSize = 'calc(var(--ag-font-size) + 1px)';
    this.eInput.style.borderWidth = 0;
    this.eInput.style.width = '95%';
    this.eInput.type = "number";
    this.eInput.min = params.min;
    this.eInput.max = params.max;
    this.eInput.step = params.step || "any";
    this.eInput.required =  params.required;
    this.eInput.placeholder =  params.placeholder || "";
    this.eInput.name = params.name;
    this.eInput.disabled = params.disabled;
    this.eInput.title = params.title || ""
  }

  // gets called once when grid ready to insert the element
  getGui() {
    return this.eInput;
  }

  // focus and select can be done after the gui is attached
  afterGuiAttached() {
    this.eInput.focus();
    this.eInput.select();
  }

  // returns the new value after editing
  getValue() {
    return this.eInput.value;
  }

  // any cleanup we need to be done here
  destroy() {
    // but this example is simple, no cleanup, we could
    // even leave this method out as it's optional
  }

  // if true, then this editor will appear in a popup
  isPopup() {
    // and we could leave this method out also, false is the default
    return false;
  }
}



