import React from 'react';
// import { Provider } from 'react-redux';
// // import { createStore } from 'redux';
import App from './components/App';
// // import reducers from './store/reducers';

// import { initializeStore } from './store';
// const store = initializeStore();

export default function Root() {
  return (
    // <Provider store={store}>
    <div>
        <App />
    </div>
    // </Provider>
  );
}