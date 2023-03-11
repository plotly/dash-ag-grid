from dash import Dash, html, dcc, register_page
from utils.utils import app_description
from utils.other_components import up_next, make_md

register_page(
    __name__, order=3, description=app_description, title="Dash AG Grid")

text1 = """
# Beyond The Basics

This is a guide on using JavaScript functions with dash-ag-grid.  Note that it's not necessary to use any
 Javascript for most of the basic and advanced features in dash-ag-grid.  However, if you would like to add custom components
 to the grid or take customization to the next level, then this tutorial is for you.


### Using JavaScript functions in dash-ag-grid props

AG Grid is a fully-featured and highly customizable JavaScript data grid. The dash-ag-grid component enables you to 
add AG Grid to your Python Dash app. However if you want to take full advantage of _all_ the great features in AG Grid,
 it's necessary to write some functions in JavaScript. 
 
You may be familiar with how to [Add JavaScript to your dash app](https://dash.plotly.com/external-resources) and how it's used in [clientside callbacks](https://dash.plotly.com/clientside-callbacks).  Here,
we'll show how JavaScript functions are passed to AG Grid from Dash props. 
   
> If you’re a Python programmer who is just getting started with JavaScript, see [JavaScript basics - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)


__Background__

Dash provides a framework that converts React components (written in JavaScript) into Python classes that
 are compatible with the Dash ecosystem.

Components in Dash are serialized as JSON. All of the props shared between the Python code and the React code ― numbers,
 strings, booleans, as well as arrays or objects containing numbers, strings, or booleans―must be serializable as JSON.
  Note that  _JavaScript functions are not valid input arguments._  However, in the AG Grid docs, you'll find that many 
  props require a JavaScript function. So, how do you do that when JavaScript functions are not valid input arguments
   in Dash?  In dash-ag-grid we have included a way to securely execute the JavaScript functions passed to the grid from Dash.

Here's an example from the AG Grid docs on [specifying selectable rows](https://www.ag-grid.com/react-data-grid/row-selection/#specify-selectable-rows)

```
const isRowSelectable = rowNode => rowNode.data ? rowNode.data.year < 2007 : false;

<AgGridReact isRowSelectable={isRowSelectable}></AgGridReact>

```  
This makes all the rows with the the year less than 2007 selectable.  Here's how you would do it in Dash:

```
dag.AgGrid(    
    dashGridOptions = {'isRowSelectable': {"function": "params.data ? params.data.year < 2007 : false" }},
)
```
See the full example in the dash-ag-grid docs [Selection checkbox section](https://dashaggrid.pythonanywhere.com/selection/selection-checkbox)
   
   
 


__Writing Secure Dash Apps__

Executing JavaScript functions passed as a prop can introduce security risks - similar to using
 the `exec()` function in Python.  To reduce the risk of remote code execution attacks, only functions included in the
  `dashAgGridFunctions` namespace will be executed.  Certain JavaScript functions are automatically included in this
  namespace, such as `Number()`, `Math()` and basic string methods such as `toUpperCase()`  You can include others by adding
  them to `dashAgGridFunctions` namespace in a .js file in the assets folder.


> 
> In a browser environment, the `window` object is the global namespace.  Any JavaScript variable defined in the `window`
 object can be passed as a component property in Dash. Only functions included in the `window.dashAgGridFunctions` object
  will be  executed in dash-ag-grid. 

__Adding simple JavaScript functions in-line__

Some functions are already added to the namespace, and can be included in-line, like in this example:

```
columnDefs = [   
    {
        "field": "balance",
        "valueFormatter": {"function": "'$' + (params.value)"},
    },
]
```

This function is passed to the `valueFormatter` prop.  It will  prepend a dollar sign to each value in the "balance" column.
For more examples see the [Value Formatters Intro Section](https://dashaggrid.pythonanywhere.com/rendering/value-formatters-intro)



__Adding functions to the `dashAgGridFunctions` namespace__

For functions that are not already added to the namespace, or are longer than a single line, you can add them by 
creating a `dashAgGridFunctions.js` file in the assets folder.   Learn more about [adding custom JavaScript](https://dash.plotly.com/external-resources) to your apps in the dash docs.
 
Note that the functions must to be added to the `dashAgGridFunctions` namespace. Here is an example:
```
var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};


dagfuncs.EUR = function(number) {
  return Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(number);
}
```


Then use the `EUR` function you defined in the `columnDefs` like this:
```
columnDefs = [
     {"headerName": "Euro", "field": "Euros", "valueFormatter": {"function": "EUR(params.value)"}},
]
```
You can find the full example in the [Value Formatters Custom Functions](https://dashaggrid.pythonanywhere.com/rendering/value-formatters-custom-functions) section.




__AG Grid `params`__


In the above example, you can see `params.value` is used in the function.  The params that can be used depends on which
 AG Grid prop you are passing the function to.  You can find more info the AG Grid docs. For example if you go
  to the [Value Formatters section of the AG Grid docs](https://www.ag-grid.com/react-data-grid/value-formatters/) and
   click on the  `ValueFormatterFunc`  you will see the options available :

![aggrid-params](https://user-images.githubusercontent.com/72614349/223864592-08258816-023b-44b2-a5e8-6bb3786a4692.png)

__Debugging JavaScript functions in dash-ag-grid__

As of V2.0.0a4, we have added a `log()` function.   Here's a [preview](https://github.com/plotly/dash-ag-grid/pull/76)
More details coming soon.

"""

layout = html.Div(
    [
        make_md(text1),
    ],
)


