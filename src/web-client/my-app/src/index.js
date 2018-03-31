import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Map from './map/Map';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<Map />, document.getElementById('root'));
registerServiceWorker();
