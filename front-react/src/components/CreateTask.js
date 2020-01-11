import React from 'react'
import backend from '../apis/backend'

class TaskStatus extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            value:'',
            file:'',
            alg:'gen'
          };
    }

    sendTask(){
        try{
            this.state.file.text().then((response)=>{
                backend.post("/create", {data: response, alg: this.state.alg});
                console.log(response);
            })
        }
        catch(e){
            console.log("No File ")
        }
    }

    handleChange(event) {
        this.setState({value: event.target.value});
        this.setState({file: event.target.files[0]});
        console.log(event.target.files[0])
    }
    
    componentDidUpdate(){
        console.log(this.state)
    }


    render () {
        return <div className="ui segment">
            <div className='message-box'>
            <button className="ui basic button " onClick={()=> {
                    console.log("CLIASDF");
                    this.sendTask();
                }}>
                <i className="icon plus"></i>
                Create New task
            </button>
            <div className="ui input">
                <input type="file" placeholder="Search..." value={this.state.value} onChange={this.handleChange.bind(this)} />
            </div>
        </div>
        </div>
    }
}

export default TaskStatus;