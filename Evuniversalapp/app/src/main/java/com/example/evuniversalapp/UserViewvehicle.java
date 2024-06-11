package com.example.evuniversalapp;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.telephony.SmsManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class UserViewvehicle extends AppCompatActivity implements JsonResponse, AdapterView.OnItemClickListener {
    ListView l1;
    SharedPreferences sh;
    String[] vehicle,desc,amount,name,value,vehicle_id;
    public static String amt,vid;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_viewvehicle);
        l1=(ListView) findViewById(R.id.list);
        l1.setOnItemClickListener(this);
        sh=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) UserViewvehicle.this;
        String q = "/UserViewvehicle?log_id=" +sh.getString("log_id", "");
        q = q.replace(" ", "%20");
        JR.execute(q);

    }

    @Override
    public void response(JSONObject jo) {
        try {

            String status = jo.getString("status");
            Log.d("pearl", status);


            if (status.equalsIgnoreCase("success")) {
                JSONArray ja1 = (JSONArray) jo.getJSONArray("data");
                vehicle = new String[ja1.length()];
                desc = new String[ja1.length()];
                amount = new String[ja1.length()];
                name = new String[ja1.length()];
                vehicle_id = new String[ja1.length()];

                value = new String[ja1.length()];



                String[] value = new String[ja1.length()];

                for (int i = 0; i < ja1.length(); i++) {
                    vehicle[i] = ja1.getJSONObject(i).getString("vehicle");

                    desc[i] = ja1.getJSONObject(i).getString("desc");
                    amount[i] = ja1.getJSONObject(i).getString("amount");
                    name[i] = ja1.getJSONObject(i).getString("name");
                    vehicle_id[i] = ja1.getJSONObject(i).getString("vehicle_id");



                    value[i] = "vehicle:" + vehicle[i] + "\ndesc: " + desc[i] + "\n amount: " + amount[i] + "\nname: " + name[i]  ;

                }
                ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), R.layout.custtext, value);

                l1.setAdapter(ar);

            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();

        }
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {

        amt=amount[i];
        vid=vehicle_id[i];


        final CharSequence[] items = {"Book Now","Cancel"};

        AlertDialog.Builder builder = new AlertDialog.Builder(UserViewvehicle.this);
        builder.setItems(items, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int item) {

                if (items[item].equals("Book Now")) {


                    startActivity(new Intent(getApplicationContext(), UserBookNow.class));



                }



                else if (items[item].equals("Cancel")) {


                    dialog.dismiss();
                }
            }

        });
        builder.show();
    }
}