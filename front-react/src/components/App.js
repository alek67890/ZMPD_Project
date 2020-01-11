import React from 'react';
// import MapComponent from './MapComponent';
// import StatusISS from './StatusISS'
import TaskList from './TaskList'
import CreateTask from './CreateTask'


class App extends React.Component {
    render(){
        return (
            <div className="ui container">
                <div className="ui segment">
                <TaskList />
                <CreateTask />
                </div>
            </div>
        )
    }
}

export default App;