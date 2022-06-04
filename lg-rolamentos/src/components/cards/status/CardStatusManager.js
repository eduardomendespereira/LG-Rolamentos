import {Card, CardBody} from "reactstrap";
import css from "./CardStatusManager.css";

const actives = localStorage.getItem("actives");
const inactives = localStorage.getItem("inactives");


function CardStatusManager(){
    return(
        <Card className="cardInfoManager">
            <div className="textosManager">
                <h2 style={{color: "grey"}}>Gerentes</h2>
                <h5 style={{color: "grey"}}></h5>
            </div>
            <div className="cardStatusManager">
                <Card className="cardAtivoManager">
                    <CardBody>
                        <h5>Gerentes Ativos: {actives}</h5>
                    </CardBody>
                </Card>
                <Card className="cardInativoManager">
                    <CardBody>
                        <h5>Gerentes Inativos: {inactives}</h5>
                    </CardBody>
                </Card>
            </div>
        </Card>
    );
}

export default CardStatusManager;