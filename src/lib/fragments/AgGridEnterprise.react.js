import React, {Component, lazy, Suspense} from 'react';
import 'ag-grid-enterprise';
import DashAgGrid from './AgGrid.react';
import { LicenseManager } from  'ag-grid-enterprise'

export default class DashAgGridEnterprise extends Component {
    render() {
        if (this.props.licenseKey) {
                LicenseManager.setLicenseKey(this.props.licenseKey);
            }
        return (<DashAgGrid {...this.props}/>);
    }

}