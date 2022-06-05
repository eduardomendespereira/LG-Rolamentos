import css from "./FormDeleteMerit.css";
import { useParams } from 'react-router';

export default function FormInactiveManager(){
    const {id} = useParams()

    return (
        <div className="formDelMerit">
            <form className="formIn" action={"http://127.0.0.1:8000/delete-merit/" + id + "/"} method="post">
                <label className="label">Tem certeza que deseja excluir o mérito do funcionário {id} ?</label>
                <input className="respostaInact" type="submit" value="Excluir"></input>
            </form>
        </div>
    )
}