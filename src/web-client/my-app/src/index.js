import React, { Component }  from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Map from './map/Map';
import registerServiceWorker from './registerServiceWorker';
import 'bootstrap/dist/css/bootstrap.css';
import { Provider as AlertProvider } from 'react-alert'
import AlertTemplate from 'react-alert-template-basic'

const options = {
    timeout: 5000,
    position: "bottom center"
};

class Root extends Component  {
    render () {
      return (
        <AlertProvider template={AlertTemplate} {...options}>
          <Map />
        </AlertProvider>
      )
    }
  }

ReactDOM.render(<Root />, document.getElementById('root'));
registerServiceWorker();
