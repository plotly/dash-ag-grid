export default {
    agGrid: () =>
        import(/* webpackChunkName: "dashaggrid" */ './fragments/AgGrid.react'),
    agGridEnterprise: () =>
        import(/* webpackChunkName: "dashaggrid" */ './fragments/AgGridEnterprise.react'),
};
