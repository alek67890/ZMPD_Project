import React from 'react'
// import ReactDOM from 'react-dom'
import TaskStatus from './TaskStatus'
import backend from '../apis/backend'

class TaskList extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            data_keys : [],
            data : {},
          };
    }
    componentDidMount(){

        this.interval = setInterval(() => backend.get('/tasks').then((response) => {
            this.setState({data_keys : response.data.keys});
            this.setState({data : response.data.data});
       }), 1000);

    }

    componentWillUnmount() {
        clearInterval(this.interval);
      }

    render (){
        return <div className='message-box'>
            {this.state.data_keys.map(( item, key ) => {
                let element = this.state.data[item]
                if (element){
                    return <TaskStatus key={key} 
                            name={element.name}
                            status={element.status}
                            output={element.output}
                            progress={element.progress}
                            points={element.points}
                            routes_plot={element.routes_plot}
                            total_load={element.total_load}
                            total_distance={element.total_distance}
                            />
                }
                return ""
                })
            }
        </div>
    }
}

export default TaskList;