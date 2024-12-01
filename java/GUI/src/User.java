import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Scanner;

public class User {
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        JLabel label = new JLabel();
        JLabel label2 = new JLabel();
        JPanel panel = new JPanel();
        JButton button = new JButton();
        JTextField textField = new JTextField();
        JTextField textField2 = new JTextField();
        button.setText("Click Me");
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(null, "Hello" + textField.getText()+" " + "Your age is "+ textField2.getText());
            }
        });
        textField.setColumns(20);
        textField2.setColumns(20);
        label.setText("Enter your name >> ");
        label2.setText("Enter your age >> ");
        frame.setSize(300, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        panel.add(label);
        panel.add(textField);
        panel.add(label2);
        panel.add(textField2);
        panel.add(button);
        frame.add(panel);
    }
}
