from dash import Dash, html, dcc, register_page
from utils.code_and_show import example_app, make_tabs
from utils.utils import app_description
from utils.other_components import up_next, make_md, make_feature_card


register_page(
    __name__, order=3, description=app_description, title="Dash AG Grid - Beyond the Basics")

text1 = """
# Beyond The Basics

This is a guide on using JavaScript functions with dash-ag-grid.  Note that it's not necessary to use any
 Javascript for most features in dash-ag-grid.  However, if you would like to add custom components
 to the grid or take customization to the next level, then this tutorial is for you.


### Using JavaScript functions in dash-ag-grid props

AG Grid is a fully-featured and highly customizable JavaScript data grid. The dash-ag-grid component enables you to 
add AG Grid to your Python Dash app. However if you want to take full advantage of _all_ the great features in AG Grid,
 it's necessary to write some functions in JavaScript. 
 
You may be familiar with how to [Add JavaScript To Your Dash App](https://dash.plotly.com/external-resources) and how it's used in [Clientside Callbacks](https://dash.plotly.com/clientside-callbacks).  Here,
we'll show how JavaScript functions are passed to AG Grid from Dash props. 
   
> If you’re a Python programmer who is just getting started with JavaScript, see:
 - [MDM - JavaScript basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
 - [MDM - JavaScript Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)


__Background__

Dash provides a framework that converts React components (written in JavaScript) into Python classes that
 are compatible with the Dash ecosystem.

Components in Dash are serialized as JSON. All of the props shared between the Python code and the React code ― numbers,
 strings, booleans, as well as arrays or objects containing numbers, strings, or booleans―must be serializable as JSON.
  Note that  _JavaScript functions are not valid input arguments._  However, in the AG Grid docs, you'll find that many 
  props require a JavaScript function as input. So, how do you do that when JavaScript functions are not valid input arguments
   in Dash?  In dash-ag-grid we have included a way to securely execute the JavaScript functions passed to the grid from Dash.

Here's an example from the AG Grid React docs on [specifying selectable rows](https://www.ag-grid.com/react-data-grid/row-selection/#specify-selectable-rows)
This makes all the rows with the the year less than 2007 selectable:

```
const isRowSelectable = rowNode => rowNode.data ? rowNode.data.year < 2007 : false;

<AgGridReact isRowSelectable={isRowSelectable}></AgGridReact>

```  
Here's how to do it in Dash:
(See the full example in the dash-ag-grid docs [Selection checkbox section](https://dashaggrid.pythonanywhere.com/selection/selection-checkbox))

```
dag.AgGrid(    
    dashGridOptions = {'isRowSelectable': {"function": "params.data ? params.data.year < 2007 : false" }},
)
```




The function is passed to the dash prop as JSON like this:

```
{"function": "params.data ? params.data.year < 2007 : false" }
```

Under the covers, Dash will take the value of this dict and parse it into a JavaScript function with a model
 of `(params) => function`.  It then passes this function to the AG Grid `isRowSelectable` prop.  
 
   
 
__Writing Secure Dash Apps__

Executing JavaScript functions passed as a prop can introduce security risks - similar to using
 the `exec()` function in Python.  To reduce the risk of remote code execution attacks, __only functions included
 in the component's namespace will be executed.__  

You can include JavaScript functions in the component's namespace by adding by them to  `dashAgGridFunctions` namespace in a .js file in the assets folder.
The functions defined in the `window.dashAgGridFunctions` object are added to the grid's namespace.  (The same applies
 when  creating <dccLink href='/components/cell-renderer' children='custom components' /> except you would use the
  `dashAgGridComponentFunctions` namespace.) 

For convenience, we include a few JavaScript functions in the the dash-ag-grid component's namespace such as:
- `Number()` and `Math()` 
- [d3-format](https://github.com/d3/d3-format) and [d3-time-format](https://github.com/d3/d3-time-format)  libraries - making it easy to format numbers and dates.
    See [Value Formatters with d3](https://dashaggrid.pythonanywhere.com/rendering/value-formatters-with-d3-format) for
     more details. 
- `log()` - This is a special Dash function for debugging in-line functions  - see more information below. 

This means you can use `Number()`, `Math()`, `d3` and `log()` in-line in your dash app without having to add
      them to a .js file in the assets folder.
 
> 
> In a browser environment, the `window` object is the global namespace.  Any JavaScript variable defined in the `window`
 object can be passed as a component property in Dash. Only functions included in the grid's namespace will be executed.
 
 

__Adding simple JavaScript functions in-line__

Simple functions like `+ - *` operators, string methods, and functions already included in the namespace such as
 `Number()`,  `Math()` and `d3` can be used in-line without adding them to the `dashAgGridFunctions` namespace.  Here is
  an example of a function to prepends a dollar sign to each value in the "balance" column:

```
columnDefs = [   
    {
        "field": "balance",
        "valueFormatter": {"function": "'$' + (params.value)"},
    },
]
```

For more examples see the [Value Formatters Intro Section](https://dashaggrid.pythonanywhere.com/rendering/value-formatters-intro)



__Adding functions to the `dashAgGridFunctions` namespace__

For functions that are not already added to the namespace, or are longer than a single line, you can add them by 
creating a `dashAgGridFunctions.js` file in the assets folder.   Learn more about [adding custom JavaScript](https://dash.plotly.com/external-resources) to your apps in the dash docs.
 
Note that the functions must to be added to the `dashAgGridFunctions` namespace. Here is an example of defining a
 function named `EUR` to format currency in the Germany locale `de-DE`.  This will format 1234.567 as 1.234,57 €
```
var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};


dagfuncs.EUR = function(number) {
  return Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(number);
}
```


Here is an example of using this `EUR` function in Dash in the `columnDefs` ::
```
columnDefs = [
     {"headerName": "Euro", "field": "Euros", "valueFormatter": {"function": "EUR(params.value)"}},
]
```
You can find the full example in the [Value Formatters Custom Functions](https://dashaggrid.pythonanywhere.com/rendering/value-formatters-custom-functions) section.

You can see all the functions we use in these docs in [GitHub](https://github.com/plotly/dash-ag-grid/blob/dev/docs/assets/dashAgGridFunctions.js)



__AG Grid `params`__


In the above example, you can see `params.value` is used in the function.  The params that can be used depends on which
 AG Grid prop you are passing the function to.  You can find more info the AG Grid docs. For example if you go
  to the [Value Formatters section of the AG Grid docs](https://www.ag-grid.com/react-data-grid/value-formatters/) and
   click on the  `ValueFormatterFunc`  you will see the options available :

![aggrid-params-valueformatter](https://user-images.githubusercontent.com/72614349/223864592-08258816-023b-44b2-a5e8-6bb3786a4692.png)

If you go to the `isRowSelectable` function , you will see there is only one option, which is the `node`:

![aggrid-params-isrowslectable](https://user-images.githubusercontent.com/72614349/236876053-d9b59864-8c03-4c5e-830f-360322d2e999.png)

All the options are positional arguments, and in Dash, they are passed to the function as `params`.  To see what options
 are available to use in the function, you can use `log()`.  The example below shows how to use `log()` to see what
  params are available with the `valueFormatter` prop.

### Debugging JavaScript functions in dash-ag-grid

To make it easier to debug in-line JavaScript functions in your Dash app, you can use the `log()` function.  This calls the `console.log()`
 method to log messages to the browser's console. The message may be one or more strings and/or JavaScript objects.
 This makes it easy to see details about which options are available for use in the `params`.

#### Example:  Debugging
This is the app from the <dccLink href='/rendering/value-formatters-intro' children='valueFormatters Intro' /> section.

Instead of formatting the "quantity" column, we are going to log `params.value` and `params` to the console

```
columnDefs = [
    {
        "field": "quantity",
      #  "valueFormatter": {"function": "d3.format(',.1f')(params.value)"},
        "valueFormatter": {"function": "log('params.value:', params.value, 'All valueFormatter params:', params)"},
    },
]

```


"""

img = "https://user-images.githubusercontent.com/72614349/226123326-17434a85-2a6a-470f-9f6d-f188f5dd299b.png"


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.getting_started.debugging_functions", make_layout=make_tabs),
        make_feature_card(img,"")

    ],
)


