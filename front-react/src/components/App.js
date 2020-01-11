import React from 'react';
// import MapComponent from './MapComponent';
// import StatusISS from './StatusISS'
import TaskList from './TaskList'
import CreateTask from './CreateTask'
import PlotCompoment from './PlotCompoment';
import PlotCompoment2 from './PlotCompoment2';


class App extends React.Component {
    render(){
        return (
            <div className="ui container">
                <div className="ui segment">
                <TaskList />
                <CreateTask />
                <PlotCompoment />
                <PlotCompoment2 />
                </div>
            </div>
        )
    }
}

export default App;