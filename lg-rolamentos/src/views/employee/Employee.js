import React from 'react';
import TableEmployee from "../../components/table/TableEmployee";
import css from "./Employee.css";

function Employee(){
    return(
        <div className="containerEmployee">
            <TableEmployee />
        </div>
    );
}
export default Employee;