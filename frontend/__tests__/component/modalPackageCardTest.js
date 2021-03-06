import React from 'react';
import ModalPackageCard from '../../assets/js/components/cards/ModalPackageCard';
import {Button} from "semantic-ui-react";
import {mount} from 'enzyme';



describe('Test render ModelPackageCard', () => {

    it('test button props', () => {
        const component = mount(<ModalPackageCard  button = {<Button basic color='green'>{1}</Button>}/>);
        expect(component.prop('button')).toEqual(
            <Button basic color='green'>{1}</Button>
        );
    });

    it('test plataform props', () => {
        const component = mount(<ModalPackageCard  plataform = "Windows" />);
        expect(component.prop('plataform')).toEqual(
            "Windows"
        );
    });

});
