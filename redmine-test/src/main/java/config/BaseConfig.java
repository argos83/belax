package config;

import org.yaml.snakeyaml.Yaml;

import java.io.InputStream;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public abstract class BaseConfig {

    protected static String[] dirs = {"general", "override"};
    protected Map<String, Object> settings;

    protected BaseConfig(String yamlBaseName){
        Yaml yaml = new Yaml();


        settings = new HashMap<>();

        for(String dir : Arrays.asList(dirs)){
            InputStream is = BaseConfig.class.getResourceAsStream("/config/" + dir + "/" + yamlBaseName + ".yml");
            if (is != null){
                Map<String, Object> override = (Map<String, Object>) yaml.load(is);
                if (override != null){
                    settings.putAll(override);
                }
            }
        }
    }

}


