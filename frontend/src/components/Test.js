import React from "react";
import axios from "axios";
export default class Test extends React.Component {
    state = {
      persons: []
    }
  
    componentDidMount() {
      axios.get(`http://127.0.0.1:8000/api/users/`)
        .then(res => {
          const persons = res.data;
          console.log(res)
          this.setState({ persons });
        })
    }

   
  
    render() {
      return (
        // <ul>
        //   {
        //     this.state.persons
        //       .map(person =>
        //         <li key={person.id}>{person.}</li>
        //       )
        //   }
        // </ul>
        <div></div>
      )
    }
  }