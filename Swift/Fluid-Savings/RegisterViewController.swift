//
//  RegisterViewController.swift
//  Fluid-Savings
//
//  Created by Tej Vuligonda on 5/22/16.
//  Copyright © 2016 Tej Vuligonda. All rights reserved.
//

import UIKit

class RegisterViewController: UIViewController {

    @IBOutlet weak var registerEmail: UITextField!
    @IBOutlet weak var registerPassword: UITextField!
    @IBOutlet weak var registerPasswordRepeat: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func registerButtonClicked(sender: AnyObject) {
        let email = registerEmail.text
        let password = registerPassword.text
        let passwordRepeat = registerPasswordRepeat.text
        
        if (email!.isEmpty || password!.isEmpty || passwordRepeat!.isEmpty) {
            displayMyAlertMessage("Please fill out all fields.")
            
            return;
        }
        
        if (registerPassword != registerPasswordRepeat) {
            displayMyAlertMessage("The two passwords do not match.")
            return;
        }
        
        
        
        
        // Store data

    }
    
    func displayMyAlertMessage(userMessage:String)
    {
        
        let myAlert = UIAlertController(title:"Alert", message:userMessage, preferredStyle: UIAlertControllerStyle.Alert);
        
        let okAction = UIAlertAction(title:"Ok", style:UIAlertActionStyle.Default, handler:nil);
        
        myAlert.addAction(okAction);
        
        self.presentViewController(myAlert, animated:true, completion:nil);
        
    }

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
