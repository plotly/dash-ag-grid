export default {
    agGrid: () =>
        import(/* webpackChunkName: "community" */ './fragments/AgGrid.react'),
    agGridEnterprise: () =>
        import(/* webpackChunkName: "enterprise" */ './fragments/AgGridEnterprise.react'),
};
